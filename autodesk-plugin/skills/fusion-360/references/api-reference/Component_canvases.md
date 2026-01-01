# Component.canvases Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Returns the canvases collection associated with this component. This provides access to the existing canvases and supports the creation of new canvases.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. Ptr<Canvases> propertyValue = component_var->canvases(); ``` ```` |

## Property Value

This is a read only property whose value is a [Canvases](Canvases.htm).

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |