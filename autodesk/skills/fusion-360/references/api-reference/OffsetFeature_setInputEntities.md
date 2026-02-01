# OffsetFeature.setInputEntities Method

Parent Object: [OffsetFeature](OffsetFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFeature.h>

## Description

Sets the faces and sheet bodies to offset.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFeature\_var" is a variable referencing an [OffsetFeature](OffsetFeature.htm) object.```` ``` # Uses no optional arguments. returnValue = offsetFeature_var.setInputEntities(entities)  # Uses optional arguments. returnValue = offsetFeature_var.setInputEntities(entities, isChainSelection) ``` ```` |

"offsetFeature\_var" is a variable referencing an [OffsetFeature](OffsetFeature.htm) object.  ```` ``` #include <Fusion/Features/OffsetFeature.h>  // Uses no optional arguments. returnValue = offsetFeature_var->setInputEntities(entities);  // Uses optional arguments. returnValue = offsetFeature_var->setInputEntities(entities, isChainSelection); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| entities | [ObjectCollection](ObjectCollection.htm) | An ObjectCollection containing the BRepFace objects to offset. Additional faces may be automatically used depending on the value of the isChainSelection argument. Input faces need not be from the same body. |
| isChainSelection | boolean | A boolean value for setting whether or not faces that are tangentially connected to the input faces (if any) will also be offset. The default value is true.   This is an optional argument whose default value is True. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |