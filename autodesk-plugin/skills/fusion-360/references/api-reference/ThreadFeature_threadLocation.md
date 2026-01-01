# ThreadFeature.threadLocation Property

Parent Object: [ThreadFeature](ThreadFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeature.h>

## Description

Gets and sets where the thread length is measured from. This property is only used in the case where the isFullLength property is false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeature\_var" is a variable referencing a ThreadFeature object.  ```` ``` # Get the value of the property. propertyValue = threadFeature_var.threadLocation  # Set the value of the property. threadFeature_var.threadLocation = propertyValue ``` ```` |

"threadFeature\_var" is a variable referencing a ThreadFeature object. ```` ``` #include <Fusion/Features/ThreadFeature.h>  // Get the value of the property. ThreadLocations propertyValue = threadFeature_var->threadLocation();  // Set the value of the property, where value_var is a ThreadLocations. bool returnValue = threadFeature_var->threadLocation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ThreadLocations](ThreadLocations.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |