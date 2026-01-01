# ArrangeFeature.unusedComponents Property

Parent Object: [ArrangeFeature](ArrangeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeature.h>

## Description

Returns an array of ArrangeComponent objects that did not fit in the arrangement. This is most useful in the case where partial arrange has been enabled, which means some components may have been arranged and others were left out.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeFeature\_var" is a variable referencing an ArrangeFeature object.  ```` ``` # Get the value of the property. propertyValue = arrangeFeature_var.unusedComponents ``` ```` |

"arrangeFeature\_var" is a variable referencing an ArrangeFeature object. ```` ``` #include <Fusion/Arrange/ArrangeFeature.h>  // Get the value of the property. std::vector<Ptr<ArrangeComponent>> propertyValue = arrangeFeature_var->unusedComponents(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [ArrangeComponent](ArrangeComponent.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |