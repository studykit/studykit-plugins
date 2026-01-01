# StitchFeatureInput.stitchSurfaces Property

Parent Object: [StitchFeatureInput](StitchFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/StitchFeatureInput.h>

## Description

Gets and sets the surfaces to stitch together.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stitchFeatureInput\_var" is a variable referencing a StitchFeatureInput object. |

"stitchFeatureInput\_var" is a variable referencing a StitchFeatureInput object. ```` ``` #include <Fusion/Features/StitchFeatureInput.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = stitchFeatureInput_var->stitchSurfaces();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = stitchFeatureInput_var->stitchSurfaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |