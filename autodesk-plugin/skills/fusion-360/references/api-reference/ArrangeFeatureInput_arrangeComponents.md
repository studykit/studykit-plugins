# ArrangeFeatureInput.arrangeComponents Property

Parent Object: [ArrangeFeatureInput](ArrangeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeatureInput.h>

## Description

Returns the ArrangeComponents object associated with this input. Use this to add and define the components that will be arranged.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeFeatureInput\_var" is a variable referencing an ArrangeFeatureInput object. |

"arrangeFeatureInput\_var" is a variable referencing an ArrangeFeatureInput object. ```` ``` #include <Fusion/Arrange/ArrangeFeatureInput.h>  // Get the value of the property. Ptr<ArrangeComponents> propertyValue = arrangeFeatureInput_var->arrangeComponents(); ``` ```` |

## Property Value

This is a read only property whose value is an [ArrangeComponents](ArrangeComponents.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |