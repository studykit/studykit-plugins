# Attributes.item Method

Parent Object: [Attributes](Attributes.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Attributes.h>

## Description

Returns the specified attribute using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"attributes\_var" is a variable referencing an [Attributes](Attributes.htm) object.```` ``` returnValue = attributes_var.item(index) ``` ```` |

"attributes\_var" is a variable referencing an [Attributes](Attributes.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Attribute](Attribute.htm) | Returns the specified attribute or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the attribute within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |