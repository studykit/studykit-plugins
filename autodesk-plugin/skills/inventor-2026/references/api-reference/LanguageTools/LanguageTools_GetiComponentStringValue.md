# LanguageTools.GetiComponentStringValue Method

Parent Object: [LanguageTools](../LanguageTools/LanguageTools.md)

## Description

Method that returns the logical value of the input iComponent string. For instance, if the input string is 'Include', a value of True is returned. The input string can be in any of the supported localized languages.

## Remarks

This method will only deal with strings that have a Boolean value associated with them. For instance, if any of the following strings is input, the return value from the method will be True: \* Include (English) \* Einschlieen (German) \* Inclure (French) \* Incluir (Spanish) \* Yes (Synonym) \* yes (Synonym) \* YES (Synonym) \* 1 (Synonym) This method will not work with strings that don't have a clear Boolean value, for example: \* Family \* Designation \* Class

## Syntax

LanguageTools.**GetiComponentStringValue**( ***iComponentString*** As String ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| iComponentString | String | Return the logical value of this string. |

## Version

Introduced in version 2008
