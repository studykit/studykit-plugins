# TangentRelationships.add Method

Parent Object: [TangentRelationships](TangentRelationships.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/TangentRelationships.h>

## Description

Creates a new tangent relationship between two components.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tangentRelationships\_var" is a variable referencing a [TangentRelationships](TangentRelationships.htm) object.```` ``` returnValue = tangentRelationships_var.add(input) ``` ```` |

"tangentRelationships\_var" is a variable referencing a [TangentRelationships](TangentRelationships.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TangentRelationship](TangentRelationship.htm) | Returns the newly created TangentRelationship or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [TangentRelationshipInput](TangentRelationshipInput.htm) | The TangentRelationshipInput object that defines the geometry and various inputs that fully define a tangent relationship. A TangentRelationshipInput object is created using the TangentRelationships.createInput method. |

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |