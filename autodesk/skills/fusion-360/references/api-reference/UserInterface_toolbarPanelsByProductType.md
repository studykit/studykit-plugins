# UserInterface.toolbarPanelsByProductType Method

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

Gets all of the toolbar panels associated with the specified product.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterface\_var" is a variable referencing a [UserInterface](UserInterface.htm) object.```` ``` returnValue = userInterface_var.toolbarPanelsByProductType(productType) ``` ```` |

"userInterface\_var" is a variable referencing a [UserInterface](UserInterface.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ToolbarPanelList](ToolbarPanelList.htm) | Returns a list of the toolbars associated with the specified product. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| productType | string | The name of the product that you want the associated workspaces for. The full list of available products can be obtained by using the Application.supportedProductTypes property. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |