# Component.id Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Returns the persistent ID of the component. This ID is created with the component and does not change. Because this ID does not change, different revisions of the same design or copies of the design asset/file will retain this ID. If components from different designs have the same ID, it indicates they are either different revisions or a copy of the design was made. Therefore, this ID will always be unique within a single design, but may not be unique in an assembly where externally referenced designs include different revisions or copies of a design.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object.  ```` ``` # Get the value of the property. propertyValue = component_var.id ``` ```` |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. string propertyValue = component_var->id(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |