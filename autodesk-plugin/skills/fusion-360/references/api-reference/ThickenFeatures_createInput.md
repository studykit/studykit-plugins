# ThickenFeatures.createInput Method

Parent Object: [ThickenFeatures](ThickenFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeatures.h>

## Description

Creates a ThickenFeatureInput object. Use properties and methods on this object to define the Thicken feature you want to create and then use the Add method, passing in the ThickenFeatureInput object to create the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"thickenFeatures\_var" is a variable referencing a [ThickenFeatures](ThickenFeatures.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"thickenFeatures\_var" is a variable referencing a [ThickenFeatures](ThickenFeatures.htm) object.  ```` ``` #include <Fusion/Features/ThickenFeatures.h>  // Uses no optional arguments. returnValue = thickenFeatures_var->createInput(inputFaces, thickness, isSymmetric, operation);  // Uses optional arguments. returnValue = thickenFeatures_var->createInput(inputFaces, thickness, isSymmetric, operation, isChainSelection); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ThickenFeatureInput](ThickenFeatureInput.htm) | Returns the newly created ThickenFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputFaces | [ObjectCollection](ObjectCollection.htm) | The faces or patch bodies to thicken. Faces need not be from the same component or body, nor do they need to be connected or touching one another. |
| thickness | [ValueInput](ValueInput.htm) | ValueInput object that defines the thickness. |
| isSymmetric | boolean | A boolean value for setting whether to add thickness symmetrically or only on one side of the face/s to thicken |
| operation | [FeatureOperations](FeatureOperations.htm) | The feature operation to perform. |
| isChainSelection | boolean | A boolean value for setting whether or not faces that are tangentially connected to the input faces (if any) will be included in the thicken. The default value is true.   This is an optional argument whose default value is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [thickenFeatures.add](thickenFeatures_add_Sample.htm) | Demonstrates the thickenFeatures.add method. |
| [Thicken Feature API Sample](ThickenFeatureSample_Sample.htm) | Demonstrates creating a new thiken feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |