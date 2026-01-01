# TemporaryBRepManager.exportToFile Method

Parent Object: [TemporaryBRepManager](TemporaryBRepManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/TemporaryBRepManager.h>

## Description

Exports the input bodies to the specified file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object.```` ``` returnValue = temporaryBRepManager_var.exportToFile(bodies, filename) ``` ```` |

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the export was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| bodies | BRepBody[] | An array of BRepBody objects that you want to export. |
| filename | string | The filename to write the BRepBody objects to. The type of file to create is inferred from the extension of the file. The valid extensions are ".sat" and ".smt". |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [TemporaryBRepManager API Sample](TemporaryBRepManager_Sample.htm) | TemporaryBRepManager related functions |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |