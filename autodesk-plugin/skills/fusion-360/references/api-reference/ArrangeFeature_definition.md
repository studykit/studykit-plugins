# ArrangeFeature.definition Property

Parent Object: [ArrangeFeature](ArrangeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeature.h>

## Description

Returns a definition object that provides access to the information defining this arrange feature and provides access to the resulting arrangement of occurrences.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeFeature\_var" is a variable referencing an ArrangeFeature object.  ```` ``` # Get the value of the property. propertyValue = arrangeFeature_var.definition ``` ```` |

"arrangeFeature\_var" is a variable referencing an ArrangeFeature object. ```` ``` #include <Fusion/Arrange/ArrangeFeature.h>  // Get the value of the property. Ptr<ArrangeDefinition> propertyValue = arrangeFeature_var->definition(); ``` ```` |

## Property Value

This is a read only property whose value is an [ArrangeDefinition](ArrangeDefinition.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |