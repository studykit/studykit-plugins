# StitchFeatures.createInput Method

Parent Object: [StitchFeatures](StitchFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/StitchFeatures.h>

## Description

Creates a StitchFeatureInput object. Use properties and methods on this object to define the stitch feature you want to create and then use the Add method, passing in the StitchFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stitchFeatures\_var" is a variable referencing a [StitchFeatures](StitchFeatures.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"stitchFeatures\_var" is a variable referencing a [StitchFeatures](StitchFeatures.htm) object.  ```` ``` #include <Fusion/Features/StitchFeatures.h>  // Uses no optional arguments. returnValue = stitchFeatures_var->createInput(stitchSurfaces, tolerance);  // Uses optional arguments. returnValue = stitchFeatures_var->createInput(stitchSurfaces, tolerance, operation); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [StitchFeatureInput](StitchFeatureInput.htm) | Returns the newly created StitchFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stitchSurfaces | [ObjectCollection](ObjectCollection.htm) | The surfaces (open BRepBodies) to stitch together. Stitching surfaces can form multiple closed volumes resulting in multiple solids. Stitch Surfaces can form multiple BRepShells (entirely connected set of entities) that would result in a single non-solid BRepBody. |
| tolerance | [ValueInput](ValueInput.htm) | ValueInput object that defines the stitching tolerance. It must define a distance value. |
| operation | [FeatureOperations](FeatureOperations.htm) | Specifies the operation type for the result when the final result is a closed solid. Otherwise this argument is ignored.   This is an optional argument whose default value is FeatureOperations.NewBodyFeatureOperation. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [stitchFeatures.add](stitchFeatures_add_Sample.htm) | Demonstrates the stitchFeatures.add method. |
| [Stitch Feature API Sample](StitchFeatureSample_Sample.htm) | Demonstrates creating a new stitch feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |