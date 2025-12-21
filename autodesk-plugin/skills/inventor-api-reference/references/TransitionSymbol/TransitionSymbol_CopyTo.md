# TransitionSymbol.CopyTo Method

Parent Object: [TransitionSymbol](../TransitionSymbol/TransitionSymbol.md)

## Description

Copies the transition symbol to specified sheet.

## Syntax

TransitionSymbol.**CopyTo**( ***TargetSheet*** As [Sheet](../Sheet/Sheet.md), [***NewName***] As Variant, [***Position***] As Variant ) As [TransitionSymbol](../TransitionSymbol/TransitionSymbol.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TargetSheet | [Sheet](../Sheet/Sheet.md) | Input Sheet object that specifies the sheet to copy the transition symbol to. |
| NewName | Variant | Optional input String value that specifies the name of the new transition symbol. If not provided the default name will be used. |
| Position | Variant | Optional input Point2d object that specifies the position on the sheet to copy the transition symbol to. If not provided the default position will be used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2025.1
