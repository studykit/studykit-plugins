# RectangularPatternFeatureInput.inputEntities Property

Parent Object: [RectangularPatternFeatureInput](RectangularPatternFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RectangularPatternFeatureInput.h>

## Description

Gets and sets the input entities. The collection can contain faces, features, bodies or occurrences. All of the entities must be of a single type. For example, it can't contain features and occurrences but only features or occurrences.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternFeatureInput\_var" is a variable referencing a RectangularPatternFeatureInput object. |

"rectangularPatternFeatureInput\_var" is a variable referencing a RectangularPatternFeatureInput object. ```` ``` #include <Fusion/Features/RectangularPatternFeatureInput.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = rectangularPatternFeatureInput_var->inputEntities();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = rectangularPatternFeatureInput_var->inputEntities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |