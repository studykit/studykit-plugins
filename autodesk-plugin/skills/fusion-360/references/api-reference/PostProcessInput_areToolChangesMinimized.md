# PostProcessInput.areToolChangesMinimized Property

Parent Object: [PostProcessInput](PostProcessInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/PostProcessInput.h>

## Description

Gets and sets that operations may be reordered between setups to minimize the number of tool changes. Operations within each setup will still be executed in the programmed order. This is commonly used for tombstone machining where you have multiple setups. The default value for this property is false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"postProcessInput\_var" is a variable referencing a PostProcessInput object. |

"postProcessInput\_var" is a variable referencing a PostProcessInput object. ```` ``` #include <Cam/CAM/PostProcessInput.h>  // Get the value of the property. boolean propertyValue = postProcessInput_var->areToolChangesMinimized();  // Set the value of the property, where value_var is a boolean. bool returnValue = postProcessInput_var->areToolChangesMinimized(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |