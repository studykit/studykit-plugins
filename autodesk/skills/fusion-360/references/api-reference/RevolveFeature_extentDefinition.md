# RevolveFeature.extentDefinition Property

Parent Object: [RevolveFeature](RevolveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeature.h>

## Description

Gets the definition object that is defining the extent of the revolve. Modifying the definition object will cause the revolve to recompute. Various types of objects can be returned depending on the type of extent currently defined for the revolve. This property returns nothing in the case where the feature is non-parametric.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeature\_var" is a variable referencing a RevolveFeature object. |

"revolveFeature\_var" is a variable referencing a RevolveFeature object. ```` ``` #include <Fusion/Features/RevolveFeature.h>  // Get the value of the property. Ptr<ExtentDefinition> propertyValue = revolveFeature_var->extentDefinition(); ``` ```` |

## Property Value

This is a read only property whose value is an [ExtentDefinition](ExtentDefinition.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |