# UnstitchFeatures.add Method

Parent Object: [UnstitchFeatures](UnstitchFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UnstitchFeatures.h>

## Description

Creates a new Unstitch feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unstitchFeatures\_var" is a variable referencing a [UnstitchFeatures](UnstitchFeatures.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"unstitchFeatures\_var" is a variable referencing a [UnstitchFeatures](UnstitchFeatures.htm) object.  ```` ``` #include <Fusion/Features/UnstitchFeatures.h>  // Uses no optional arguments. returnValue = unstitchFeatures_var->add(faces);  // Uses optional arguments. returnValue = unstitchFeatures_var->add(faces, isChainSelection); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [UnstitchFeature](UnstitchFeature.htm) | Returns the newly created UnstitchFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| faces | [ObjectCollection](ObjectCollection.htm) | The faces and/or bodies to Unstitch. Individual faces can be unstitched from solid and/or patch bodies. The faces being unstitched need not all come from the same body. |
| isChainSelection | boolean | A boolean value for setting whether or not faces that are connected and adjacent to the input faces will be included in the selection. The default value is true.   This is an optional argument whose default value is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Unstitch Feature API Sample](UnstitchFeatureSample_Sample.htm) | Demonstrates creating a new unstitch feature |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |