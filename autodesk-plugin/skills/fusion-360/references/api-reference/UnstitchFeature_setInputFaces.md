# UnstitchFeature.setInputFaces Method

Parent Object: [UnstitchFeature](UnstitchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UnstitchFeature.h>

## Description

Sets the faces and/or bodies to be unstitched.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unstitchFeature\_var" is a variable referencing a [UnstitchFeature](UnstitchFeature.htm) object.```` ``` # Uses no optional arguments. returnValue = unstitchFeature_var.setInputFaces(faces)  # Uses optional arguments. returnValue = unstitchFeature_var.setInputFaces(faces, isChainSelection) ``` ```` |

"unstitchFeature\_var" is a variable referencing a [UnstitchFeature](UnstitchFeature.htm) object.  ```` ``` #include <Fusion/Features/UnstitchFeature.h>  // Uses no optional arguments. returnValue = unstitchFeature_var->setInputFaces(faces);  // Uses optional arguments. returnValue = unstitchFeature_var->setInputFaces(faces, isChainSelection); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| faces | [ObjectCollection](ObjectCollection.htm) | The faces and/or bodies to Unstitch. Individual faces can be unstitched from solids and/or patch bodies. The faces being unstitched need not all come from the same body. |
| isChainSelection | boolean | A boolean value for setting whether or not faces that are connected and adjacent to the input faces will be included in the selection. The default value is true.   This is an optional argument whose default value is True. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |