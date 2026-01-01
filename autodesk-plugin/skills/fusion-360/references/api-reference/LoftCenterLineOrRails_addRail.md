# LoftCenterLineOrRails.addRail Method

Parent Object: [LoftCenterLineOrRails](LoftCenterLineOrRails.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftCenterLineOrRails.h>

## Description

Add a rail to the loft definition. Multiple rails can be defined, so each call of this method adds a new rail.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftCenterLineOrRails\_var" is a variable referencing a [LoftCenterLineOrRails](LoftCenterLineOrRails.htm) object.```` ``` returnValue = loftCenterLineOrRails_var.addRail(entity) ``` ```` |

"loftCenterLineOrRails\_var" is a variable referencing a [LoftCenterLineOrRails](LoftCenterLineOrRails.htm) object.  ```` ``` #include <Fusion/Features/LoftCenterLineOrRails.h>  returnValue = loftCenterLineOrRails_var->addRail(entity); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [LoftCenterLineOrRail](LoftCenterLineOrRail.htm) | Returns the new LoftCenterLineOrRail object or null in the case of a failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| entity | [Base](Base.htm) | The entity that defines the rail. This can be a single sketch curve, a single BRepEdge, or a Path consisting of connected B-Rep edges or sketch curves. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |