# BRepShellDefinitions.item Method

Parent Object: [BRepShellDefinitions](BRepShellDefinitions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepShellDefinitions.h>

## Description

Function that returns the specified BRepShellDefinition object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepShellDefinitions\_var" is a variable referencing a [BRepShellDefinitions](BRepShellDefinitions.htm) object.```` ``` returnValue = bRepShellDefinitions_var.item(index) ``` ```` |

"bRepShellDefinitions\_var" is a variable referencing a [BRepShellDefinitions](BRepShellDefinitions.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepShellDefinition](BRepShellDefinition.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |