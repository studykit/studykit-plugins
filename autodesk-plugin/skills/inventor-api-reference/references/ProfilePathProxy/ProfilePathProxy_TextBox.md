# ProfilePathProxy.TextBox Property

Parent Object: [ProfilePathProxy](../ProfilePathProxy/ProfilePathProxy.md)

## Description

Property that gets the text box this profile path was derived from. This property is only valid if the profile path denotes a text box which will be indicated by the value of the TextPath property being True. On the other hand, if the profile path denotes a set of connected curves, then this property does not apply and will return Nothing.

## Syntax

ProfilePathProxy.**TextBox**() As [TextBox](../TextBox/TextBox.md)

## Property Value

This is a read only property whose value is a [TextBox](../TextBox/TextBox.md).

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |