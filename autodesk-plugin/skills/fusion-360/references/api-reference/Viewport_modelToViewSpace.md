# Viewport.modelToViewSpace Method

Parent Object: [Viewport](Viewport.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Viewport.h>

## Description

A specified point in model space returns the equivalent point in view space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"viewport\_var" is a variable referencing a [Viewport](Viewport.htm) object.```` ``` returnValue = viewport_var.modelToViewSpace(modelCoordinate) ``` ```` |

"viewport\_var" is a variable referencing a [Viewport](Viewport.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Point2D](Point2D.htm) | Returns the equivalent point in view space. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| modelCoordinate | [Point3D](Point3D.htm) | A coordinate in model space. |

## Version

Introduced in version December 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |