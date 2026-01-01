# Component.isOriginFolderLightBulbOn Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Gets and sets if the light bulb of the origin folder as seen in the browser is on or off. This controls the visibility of the origin construction geometry.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. boolean propertyValue = component_var->isOriginFolderLightBulbOn();  // Set the value of the property, where value_var is a boolean. bool returnValue = component_var->isOriginFolderLightBulbOn(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |