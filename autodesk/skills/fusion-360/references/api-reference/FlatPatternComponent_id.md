# FlatPatternComponent.id Property

Parent Object: [FlatPatternComponent](FlatPatternComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternComponent.h>

## Description

Returns the persistent ID of the component. This ID is created with the component and does not change. Because this ID does not change, different revisions of the same design or copies of the design asset/file will retain this ID. If components from different designs have the same ID, it indicates they are either different revisions or a copy of the design was made. Therefore, this ID will always be unique within a single design, but may not be unique in an assembly where externally referenced designs include different revisions or copies of a design.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object.  ```` ``` # Get the value of the property. propertyValue = flatPatternComponent_var.id ``` ```` |

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. ```` ``` #include <Fusion/SheetMetal/FlatPatternComponent.h>  // Get the value of the property. string propertyValue = flatPatternComponent_var->id(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |