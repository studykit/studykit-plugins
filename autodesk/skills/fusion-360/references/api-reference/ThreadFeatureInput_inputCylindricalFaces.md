# ThreadFeatureInput.inputCylindricalFaces Property

Parent Object: [ThreadFeatureInput](ThreadFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeatureInput.h>

## Description

Gets and sets the cylindrical input faces.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeatureInput\_var" is a variable referencing a ThreadFeatureInput object. |

"threadFeatureInput\_var" is a variable referencing a ThreadFeatureInput object. ```` ``` #include <Fusion/Features/ThreadFeatureInput.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = threadFeatureInput_var->inputCylindricalFaces();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = threadFeatureInput_var->inputCylindricalFaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |