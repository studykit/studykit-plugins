# LanguageTools Object

## Description

The LanguageTools object provides a means of determining the logical boolean value of iPart/iComponent table strings.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetiComponentStringValue](../LanguageTools/LanguageTools_GetiComponentStringValue.md) | Method that returns the logical value of the input iComponent string. For instance, if the input string is 'Include', a value of True is returned. The input string can be in any of the supported localized languages. |
| [IsValidPrimaryModelState](../LanguageTools/LanguageTools_IsValidPrimaryModelState.md) | Method that returns whether the input primary model state string is valid or not. The input primary model state string can be in any language that Inventor supports. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../LanguageTools/LanguageTools_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [CurrentPrimaryModelStateString](../LanguageTools/LanguageTools_CurrentPrimaryModelStateString.md) | Read-only property that returns the primary ModelState string in current language. |
| [Parent](../LanguageTools/LanguageTools_Parent.md) | Property that returns the parent Application object. |
| [Type](../LanguageTools/LanguageTools_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Application.LanguageTools](../Application/Application_LanguageTools.md), [InventorServer.LanguageTools](InventorServer_LanguageTools.md), [InventorServerObject.LanguageTools](InventorServerObject_LanguageTools.md)

## Version

Introduced in version 2008
