# TransitionSymbols.CreateDefinition Method

Parent Object: [TransitionSymbols](../TransitionSymbols/TransitionSymbols.md)

## Description

Creates a new transition symbol definition.

## Syntax

TransitionSymbols.**CreateDefinition**( [***SymbolIndicationType***] As Variant, [***CombinedMaximumAndLeastMaterial***] As Variant, [***Options***] As Variant ) As [TransitionSymbolDefinition](../TransitionSymbolDefinition/TransitionSymbolDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SymbolIndicationType | Variant | Optional input TransitionSymbolIndicationTypeEnum indicating the transition symbol indication type. If not provided, this defaults to kNoSymbolIndication. |
| CombinedMaximumAndLeastMaterial | Variant | Optional input Boolean value that specifies whether to combine maximum material and least material radius boundary specification. If not provided this defaults to False.   This is an optional argument whose default value is null. |
| Options | Variant | Optional input NameValueMap to specify more options for the definition. This is reserved for future use.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2025.1

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |