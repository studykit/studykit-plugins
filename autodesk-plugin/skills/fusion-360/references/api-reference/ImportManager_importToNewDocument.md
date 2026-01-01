# ImportManager.importToNewDocument Method

Parent Object: [ImportManager](ImportManager.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ImportManager.h>

## Description

Executes the import operation to import a file (of the format specified by the input ImportOptions object) to a new document.

## Syntax

* [Python](#Python)
* [C++](#C++)

"importManager\_var" is a variable referencing an [ImportManager](ImportManager.htm) object.```` ``` returnValue = importManager_var.importToNewDocument(importOptions) ``` ```` |

"importManager\_var" is a variable referencing an [ImportManager](ImportManager.htm) object.  ```` ``` #include <Core/Application/ImportManager.h>  returnValue = importManager_var->importToNewDocument(importOptions); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Document](Document.htm) | Returns the newly created Document object or null if the creation failed. A new unnamed, unsaved document will be opened in Fusion 360 as a result. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| importOptions | [ImportOptions](ImportOptions.htm) | An ImportOptions object that is created using one of the create methods on the ImportManager object. This defines the type of file and any available options supported for that file type. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Import Manager API Sample](ImportManager_Sample.htm) | Demonstrates how to import different formats to Fusion document |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |