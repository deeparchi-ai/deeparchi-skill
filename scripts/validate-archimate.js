/**
 * ArchiMate 图表验证脚本
 * 用于验证 draw.io 导出的 XML 是否符合 ArchiMate 标准
 */

// ArchiMate 3.2 标准元素类型
const ARCHIMATE_ELEMENTS = {
  // 业务层
  business: [
    'BusinessActor',
    'BusinessRole',
    'BusinessCollaboration',
    'BusinessInterface',
    'BusinessProcess',
    'BusinessFunction',
    'BusinessInteraction',
    'BusinessEvent',
    'BusinessService',
    'BusinessObject',
    'Contract'
  ],
  // 应用层
  application: [
    'ApplicationComponent',
    'ApplicationCollaboration',
    'ApplicationInterface',
    'ApplicationFunction',
    'ApplicationInteraction',
    'ApplicationProcess',
    'ApplicationEvent',
    'ApplicationService',
    'DataObject'
  ],
  // 技术层
  technology: [
    'Node',
    'Device',
    'SystemSoftware',
    'TechnologyCollaboration',
    'TechnologyInterface',
    'Path',
    'CommunicationNetwork',
    'TechnologyFunction',
    'TechnologyProcess',
    'TechnologyInteraction',
    'TechnologyEvent',
    'TechnologyService',
    'Artifact'
  ]
};

// ArchiMate 标准关系类型
const ARCHIMATE_RELATIONS = [
  'Composition',
  'Aggregation',
  'Assignment',
  'Realization',
  'Serving',
  'Access',
  'Influence',
  'Triggering',
  'Flow',
  'Specialization',
  'Association',
  'Junction'
];

/**
 * 验证 draw.io XML 中的 ArchiMate 元素
 * @param {string} xmlContent - draw.io 导出的 XML 内容
 * @returns {Object} 验证结果
 */
function validateArchiMateDiagram(xmlContent) {
  const parser = new DOMParser();
  const xmlDoc = parser.parseFromString(xmlContent, 'text/xml');
  
  const errors = [];
  const warnings = [];
  const elements = [];
  
  // 提取所有 mxCell 元素
  const cells = xmlDoc.getElementsByTagName('mxCell');
  
  for (let cell of cells) {
    const style = cell.getAttribute('style') || '';
    const value = cell.getAttribute('value') || '';
    
    // 检查是否是 ArchiMate 元素
    if (style.includes('archimate')) {
      const elementType = extractElementType(style);
      if (elementType) {
        elements.push({
          id: cell.getAttribute('id'),
          type: elementType,
          value: value,
          layer: getElementLayer(elementType)
        });
      } else {
        warnings.push(`未知的 ArchiMate 元素类型: ${style}`);
      }
    }
    
    // 检查关系
    if (cell.getAttribute('edge') === '1') {
      const relationType = extractRelationType(style);
      if (relationType && !ARCHIMATE_RELATIONS.includes(relationType)) {
        warnings.push(`非标准关系类型: ${relationType}`);
      }
    }
  }
  
  // 验证元素命名
  elements.forEach(element => {
    if (!element.value || element.value.trim() === '') {
      errors.push(`元素 ${element.id} 缺少名称`);
    }
  });
  
  // 验证关系连接
  const relations = xmlDoc.getElementsByTagName('mxCell');
  for (let relation of relations) {
    if (relation.getAttribute('edge') === '1') {
      const source = relation.getAttribute('source');
      const target = relation.getAttribute('target');
      if (!source || !target) {
        errors.push(`关系缺少源或目标元素`);
      }
    }
  }
  
  return {
    valid: errors.length === 0,
    errors: errors,
    warnings: warnings,
    elements: elements,
    elementCount: elements.length,
    relationCount: Array.from(relations).filter(r => r.getAttribute('edge') === '1').length
  };
}

/**
 * 从样式字符串中提取元素类型
 */
function extractElementType(style) {
  const match = style.match(/archimate=([^;]+)/);
  return match ? match[1] : null;
}

/**
 * 从样式字符串中提取关系类型
 */
function extractRelationType(style) {
  const match = style.match(/edgeStyle=([^;]+)/);
  return match ? match[1] : null;
}

/**
 * 获取元素所属的层
 */
function getElementLayer(elementType) {
  const allElements = [
    ...ARCHIMATE_ELEMENTS.business,
    ...ARCHIMATE_ELEMENTS.application,
    ...ARCHIMATE_ELEMENTS.technology
  ];
  
  if (ARCHIMATE_ELEMENTS.business.includes(elementType)) {
    return 'business';
  } else if (ARCHIMATE_ELEMENTS.application.includes(elementType)) {
    return 'application';
  } else if (ARCHIMATE_ELEMENTS.technology.includes(elementType)) {
    return 'technology';
  }
  return 'unknown';
}

/**
 * 生成验证报告
 */
function generateValidationReport(validationResult) {
  let report = '# ArchiMate 图表验证报告\n\n';
  
  report += `## 验证结果\n\n`;
  report += `- **状态**: ${validationResult.valid ? '✅ 通过' : '❌ 失败'}\n`;
  report += `- **元素数量**: ${validationResult.elementCount}\n`;
  report += `- **关系数量**: ${validationResult.relationCount}\n\n`;
  
  if (validationResult.errors.length > 0) {
    report += `## 错误 (${validationResult.errors.length})\n\n`;
    validationResult.errors.forEach((error, index) => {
      report += `${index + 1}. ${error}\n`;
    });
    report += '\n';
  }
  
  if (validationResult.warnings.length > 0) {
    report += `## 警告 (${validationResult.warnings.length})\n\n`;
    validationResult.warnings.forEach((warning, index) => {
      report += `${index + 1}. ${warning}\n`;
    });
    report += '\n';
  }
  
  if (validationResult.elements.length > 0) {
    report += `## 元素统计\n\n`;
    const layerStats = {};
    validationResult.elements.forEach(element => {
      layerStats[element.layer] = (layerStats[element.layer] || 0) + 1;
    });
    
    report += '| 层 | 数量 |\n';
    report += '|---|---|\n';
    Object.entries(layerStats).forEach(([layer, count]) => {
      report += `| ${layer} | ${count} |\n`;
    });
  }
  
  return report;
}

// 导出函数（Node.js 环境）
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    validateArchiMateDiagram,
    generateValidationReport,
    ARCHIMATE_ELEMENTS,
    ARCHIMATE_RELATIONS
  };
}
