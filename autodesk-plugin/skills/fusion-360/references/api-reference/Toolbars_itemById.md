# Toolbars.itemById Method

Parent Object: [Toolbars](Toolbars.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Toolbars.h>

## Description

Returns the Toolbar of the specified ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbars\_var" is a variable referencing a [Toolbars](Toolbars.htm) object.```` ``` returnValue = toolbars_var.itemById(id) ``` ```` |

"toolbars\_var" is a variable referencing a [Toolbars](Toolbars.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Toolbar](Toolbar.htm) | Returns the toolbar with the specified ID or null if there's not a toolbar with the specified ID. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The Id of the toolbar to return. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |