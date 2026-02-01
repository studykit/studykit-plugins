# ReplaceFaceFeatureInput.sourceFaces Property

Parent Object: [ReplaceFaceFeatureInput](ReplaceFaceFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReplaceFaceFeatureInput.h>

## Description

Gets and sets the entities that define the source faces to perform replace. The collection can contain the faces from a solid and/or from features. All the faces must be on the same body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"replaceFaceFeatureInput\_var" is a variable referencing a ReplaceFaceFeatureInput object. |

"replaceFaceFeatureInput\_var" is a variable referencing a ReplaceFaceFeatureInput object. ```` ``` #include <Fusion/Features/ReplaceFaceFeatureInput.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = replaceFaceFeatureInput_var->sourceFaces();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = replaceFaceFeatureInput_var->sourceFaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |