# Component.isJointsFolderLightBulbOn Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Gets and sets if the light bulb of the joints folder as seen in the browser is on or off. This controls the visibility of the joints in this occurrence. The light bulb for the folder is component specific and will turn off the joints for all occurrences referencing the component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. boolean propertyValue = component_var->isJointsFolderLightBulbOn();  // Set the value of the property, where value_var is a boolean. bool returnValue = component_var->isJointsFolderLightBulbOn(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |