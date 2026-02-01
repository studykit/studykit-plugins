# CircularPatternFeatureInput.inputEntities Property

Parent Object: [CircularPatternFeatureInput](CircularPatternFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CircularPatternFeatureInput.h>

## Description

Gets and sets the input entities. The collection can contain faces, features, bodies or occurrences. All of the entities must be of a single type. For example, it can't contain features and occurrences but only features or occurrences.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternFeatureInput\_var" is a variable referencing a CircularPatternFeatureInput object. |

"circularPatternFeatureInput\_var" is a variable referencing a CircularPatternFeatureInput object. ```` ``` #include <Fusion/Features/CircularPatternFeatureInput.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = circularPatternFeatureInput_var->inputEntities();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = circularPatternFeatureInput_var->inputEntities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |