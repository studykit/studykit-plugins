# Scripts.addNew Method

Parent Object: [Scripts](Scripts.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Scripts.h>

## Description

Creates a new script or add-in. This uses the same internal template that's used when creating a new script or add-in using the "Scripts and Add-Ins" dialog. The provided ScriptInput object defines the information needed to create a new script or add-in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scripts\_var" is a variable referencing a [Scripts](Scripts.htm) object.```` ``` returnValue = scripts_var.addNew(input) ``` ```` |

"scripts\_var" is a variable referencing a [Scripts](Scripts.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Script](Script.htm) | Returns the newly created Script object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [ScriptInput](ScriptInput.htm) | A ScriptInput object which defines the required information to create a new script or add-in. It is created using the createNewScriptInput method. |

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |