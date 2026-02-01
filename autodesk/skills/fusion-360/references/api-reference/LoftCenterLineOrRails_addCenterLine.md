# LoftCenterLineOrRails.addCenterLine Method

Parent Object: [LoftCenterLineOrRails](LoftCenterLineOrRails.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftCenterLineOrRails.h>

## Description

Adds a centerline. A single centerline can be defined for a loft. If a centerline or rails have already been defined, they will be removed and the input will become the new single centerline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftCenterLineOrRails\_var" is a variable referencing a [LoftCenterLineOrRails](LoftCenterLineOrRails.htm) object.```` ``` returnValue = loftCenterLineOrRails_var.addCenterLine(entity) ``` ```` |

"loftCenterLineOrRails\_var" is a variable referencing a [LoftCenterLineOrRails](LoftCenterLineOrRails.htm) object.  ```` ``` #include <Fusion/Features/LoftCenterLineOrRails.h>  returnValue = loftCenterLineOrRails_var->addCenterLine(entity); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [LoftCenterLineOrRail](LoftCenterLineOrRail.htm) | Returns the new LoftCenterLineOrRail object or null in the case of a failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| entity | [Base](Base.htm) | The entity that defines the center line. This can be a single sketch curve, a single BRepEdge, a Path consisting of connected B-Rep edges or sketch curves. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |