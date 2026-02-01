# ExtendFeatureInput.edges Property

Parent Object: [ExtendFeatureInput](ExtendFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtendFeatureInput.h>

## Description

Gets and sets the edges to extend

## Syntax

* [Python](#Python)
* [C++](#C++)

"extendFeatureInput\_var" is a variable referencing an ExtendFeatureInput object. |

"extendFeatureInput\_var" is a variable referencing an ExtendFeatureInput object. ```` ``` #include <Fusion/Features/ExtendFeatureInput.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = extendFeatureInput_var->edges();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = extendFeatureInput_var->edges(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |