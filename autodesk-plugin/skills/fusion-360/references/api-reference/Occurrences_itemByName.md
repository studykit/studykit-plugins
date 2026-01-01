# Occurrences.itemByName Method

Parent Object: [Occurrences](Occurrences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrences.h>

## Description

Returns the specified occurrence using the name of the occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrences\_var" is a variable referencing an [Occurrences](Occurrences.htm) object.```` ``` returnValue = occurrences_var.itemByName(name) ``` ```` |

"occurrences\_var" is a variable referencing an [Occurrences](Occurrences.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Occurrence](Occurrence.htm) | Returns the occurrence or null if an invalid name was specified |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the occurrence to return. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |