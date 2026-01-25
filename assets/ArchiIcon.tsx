import React from "react";

export type ArchiIconType =
  | "businessActor"
  | "businessRole"
  | "businessCollaboration"
  | "businessProcess"
  | "businessFunction"
  | "businessService"
  | "businessObject"
  | "contract";

export interface ArchiIconProps {
  type: ArchiIconType;
  size?: number;
  strokeWidth?: number;
  className?: string;
  color?: string;
  fill?: string;
  title?: string;
}

const defaultSize = 24;
const defaultStrokeWidth = 2;

const renderPath = (type: ArchiIconType) => {
  switch (type) {
    case "businessActor":
      return (
        <>
          <circle cx="12" cy="7" r="4" />
          <path d="M5 21v-2a7 7 0 0 1 14 0v2" />
        </>
      );
    case "businessRole":
      return (
        <>
          <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" />
          <circle cx="9" cy="7" r="4" />
        </>
      );
    case "businessCollaboration":
      return (
        <>
          <circle cx="9" cy="12" r="6" strokeOpacity="0.5" />
          <circle cx="15" cy="12" r="6" strokeOpacity="0.5" />
        </>
      );
    case "businessProcess":
      return <path d="M5 12h14m-4-4l4 4-4 4" />;
    case "businessFunction":
      return (
        <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z" />
      );
    case "businessService":
      return <path d="M12 3a9 9 0 0 1 9 9v9H3v-9a9 9 0 0 1 9-9z" />;
    case "businessObject":
      return (
        <>
          <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
          <polyline points="14 2 14 8 20 8" />
        </>
      );
    case "contract":
      return (
        <>
          <rect x="4" y="2" width="16" height="20" rx="2" />
          <line x1="8" y1="6" x2="16" y2="6" strokeWidth="3" />
        </>
      );
    default:
      return null;
  }
};

export const ArchiIcon = ({
  type,
  size = defaultSize,
  strokeWidth = defaultStrokeWidth,
  className,
  color = "currentColor",
  fill = "none",
  title,
}: ArchiIconProps) => (
  <svg
    width={size}
    height={size}
    viewBox="0 0 24 24"
    fill={fill}
    stroke={color}
    strokeWidth={strokeWidth}
    strokeLinecap="round"
    strokeLinejoin="round"
    className={className}
    aria-hidden={title ? undefined : true}
    role={title ? "img" : "presentation"}
  >
    {title ? <title>{title}</title> : null}
    {renderPath(type)}
  </svg>
);

export const archiIconTypes: ArchiIconType[] = [
  "businessActor",
  "businessRole",
  "businessCollaboration",
  "businessProcess",
  "businessFunction",
  "businessService",
  "businessObject",
  "contract",
];
