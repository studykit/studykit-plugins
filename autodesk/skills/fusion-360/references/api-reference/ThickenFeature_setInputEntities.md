# ThickenFeature.setInputEntities Method

Parent Object: [ThickenFeature](ThickenFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeature.h>

## Description

Sets the faces and patch bodies to thicken.

## Syntax

* [Python](#Python)
* [C++](#C++)

"thickenFeature\_var" is a variable referencing a [ThickenFeature](ThickenFeature.htm) object.```` ``` # Uses no optional arguments. returnValue = thickenFeature_var.setInputEntities(inputFaces)  # Uses optional arguments. returnValue = thickenFeature_var.setInputEntities(inputFaces, isChainSelection) ``` ```` |

"thickenFeature\_var" is a variable referencing a [ThickenFeature](ThickenFeature.htm) object.  ```` ``` #include <Fusion/Features/ThickenFeature.h>  // Uses no optional arguments. returnValue = thickenFeature_var->setInputEntities(inputFaces);  // Uses optional arguments. returnValue = thickenFeature_var->setInputEntities(inputFaces, isChainSelection); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputFaces | [ObjectCollection](ObjectCollection.htm) | The faces or patch bodies to thicken. Faces need not be from the same component or body, nor do they need to be connected or touching one another. |
| isChainSelection | boolean | A boolean value for setting whether or not faces that are tangentially connected to the input faces (if any) will be included in the offset. The default value is true.   This is an optional argument whose default value is True. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |