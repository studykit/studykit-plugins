# ImportManager.createSMTImportOptions Method

Parent Object: [ImportManager](ImportManager.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ImportManager.h>

## Description

Creates an SMTImportOptions object that's used to import a design from SMT format. Creation of the SMTImportOptions object does not perform the import. You must pass this object to one of the ImportManager import methods to perform the import. The SMTImportOptions supports any available options when importing from SMT format.

## Syntax

* [Python](#Python)
* [C++](#C++)

"importManager\_var" is a variable referencing an [ImportManager](ImportManager.htm) object.```` ``` returnValue = importManager_var.createSMTImportOptions(filename) ``` ```` |

"importManager\_var" is a variable referencing an [ImportManager](ImportManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SMTImportOptions](SMTImportOptions.htm) | The created SMTImportOptions object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | string | The filename or URL of the SMT file to be imported. |

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