# CircularPatternFeature.inputEntities Property

Parent Object: [CircularPatternFeature](CircularPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CircularPatternFeature.h>

## Description

Gets and sets the input entities. The collection can contain faces, features, bodies or occurrences. All of the entities must be of a single type. For example, it can't contain features and occurrences but only features or occurrences.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternFeature\_var" is a variable referencing a CircularPatternFeature object.  ```` ``` # Get the value of the property. propertyValue = circularPatternFeature_var.inputEntities  # Set the value of the property. circularPatternFeature_var.inputEntities = propertyValue ``` ```` |

"circularPatternFeature\_var" is a variable referencing a CircularPatternFeature object. ```` ``` #include <Fusion/Features/CircularPatternFeature.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = circularPatternFeature_var->inputEntities();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = circularPatternFeature_var->inputEntities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |