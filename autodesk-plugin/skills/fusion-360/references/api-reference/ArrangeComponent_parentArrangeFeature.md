# ArrangeComponent.parentArrangeFeature Property

Parent Object: [ArrangeComponent](ArrangeComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeComponent.h>

## Description

Returns the ArrangeFeature this ArrangeComponent is associated with. This property returns null in the case where a feature hasn't been created yet and there is only an ArrangeFeatureInput.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeComponent\_var" is a variable referencing an ArrangeComponent object. |

"arrangeComponent\_var" is a variable referencing an ArrangeComponent object. ```` ``` #include <Fusion/Arrange/ArrangeComponent.h>  // Get the value of the property. Ptr<ArrangeFeature> propertyValue = arrangeComponent_var->parentArrangeFeature(); ``` ```` |

## Property Value

This is a read only property whose value is an [ArrangeFeature](ArrangeFeature.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |