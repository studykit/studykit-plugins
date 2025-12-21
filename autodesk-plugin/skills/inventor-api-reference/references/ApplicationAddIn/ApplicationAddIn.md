# ApplicationAddIn Object

## Description

Object that represents an Application AddIn inside Autodesk Inventor.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../ApplicationAddIn/ApplicationAddIn_Activate.md) | Creates and initializes the AddIn. No effect if AddIn already active. |
| [Deactivate](../ApplicationAddIn/ApplicationAddIn_Deactivate.md) | Invokes the shutdown sequence on the AddIn. No effect if AddIn inactive. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Activated](../ApplicationAddIn/ApplicationAddIn_Activated.md) | Gets a Boolean flag indicating whether this AddIn is currently active in the session. |
| [AddInType](../ApplicationAddIn/ApplicationAddIn_AddInType.md) | Gets the constant that indicates the type of this AddIn. |
| [Application](../ApplicationAddIn/ApplicationAddIn_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Automation](../ApplicationAddIn/ApplicationAddIn_Automation.md) | Property that returns the Add-in's automation interface (if any). Fails if the Add-in is currently inactive. |
| [ClassIdString](../ApplicationAddIn/ApplicationAddIn_ClassIdString.md) | Gets the CLSID of the AddIn as the string used in the class moniker. |
| [ClientId](../ApplicationAddIn/ApplicationAddIn_ClientId.md) | Property that returns a GUID in string format that uniquely identifies this Add-in. This GUID is used as an identifier when creating Add-in specific objects such as user interface elements, client features, etc. |
| [DataVersion](../ApplicationAddIn/ApplicationAddIn_DataVersion.md) | Gets and sets the current data version of the AddIn. This value corresponds to the 'Data Version' registry entry in the AddIn's registry hive. |
| [Description](../ApplicationAddIn/ApplicationAddIn_Description.md) | Gets the description of the AddIn. |
| [DisplayName](../ApplicationAddIn/ApplicationAddIn_DisplayName.md) | Gets the displayable name of the AddIn. |
| [Hidden](../ApplicationAddIn/ApplicationAddIn_Hidden.md) | Gets and sets whether the AddIn is hidden or not. |
| [LicenseStatus](../ApplicationAddIn/ApplicationAddIn_LicenseStatus.md) | Gets the license status of the AddIn. |
| [LoadAutomatically](../ApplicationAddIn/ApplicationAddIn_LoadAutomatically.md) | Gets/Sets whether the add-in loads automatically based on the load behavior specified for the add-in. If set to False, the add-in needs to be manually loaded by the user. |
| [LoadBehavior](../ApplicationAddIn/ApplicationAddIn_LoadBehavior.md) | Gets a constant indicating the load behavior (load time) of the add-in. This applies only if the LoadAutomatically property is set to True. |
| [Location](../ApplicationAddIn/ApplicationAddIn_Location.md) | Property that returns the full file name of the dll associated with this Add-in. |
| [Parent](../ApplicationAddIn/ApplicationAddIn_Parent.md) | Property that returns the parent Application object. |
| [ProgId](../ApplicationAddIn/ApplicationAddIn_ProgId.md) | Gets the ProgID of the AddIn. |
| [ShortDisplayName](../ApplicationAddIn/ApplicationAddIn_ShortDisplayName.md) | Property that returns the short display name of the Add-in. Used in places to succinctly identify the AddIn inside Inventor's UI. |
| [Type](../ApplicationAddIn/ApplicationAddIn_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UserInterfaceVersion](../ApplicationAddIn/ApplicationAddIn_UserInterfaceVersion.md) | Property that returns the version of the user interface of the add-in. Incrementing this version results in all of the add-in"s UI getting cleaned up during Inventor start-up. |
| [UserUnloadable](../ApplicationAddIn/ApplicationAddIn_UserUnloadable.md) | Gets and sets whether the AddIn is allowed to be unloaded by the user. |

## Accessed From

[ApplicationAddIns.Item](../ApplicationAddIns/ApplicationAddIns_Item.md), [ApplicationAddIns.ItemById](../ApplicationAddIns/ApplicationAddIns_ItemById.md), [ApplicationAddInSite.Parent](../ApplicationAddInSite/ApplicationAddInSite_Parent.md)

## Derived Classes

[TranslatorAddIn](../TranslatorAddIn/TranslatorAddIn.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Export to IFC Format Sample](../../sample-programs/ExportToIFCFormatSample_Sample.md) | This sample demonstrates how to export an assembly to IFC format. |

## Version

Introduced in version 4
