# ModelHoleThreadNoteDefinition.FormattedHoleThreadNote Property

Parent Object: [ModelHoleThreadNoteDefinition](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition.md)

## Description

Read-write property that gets and sets the fully formatted string that defines the contents of the hole or thread text.
The formatting is specified using XML tags within the string. By default, all text in the string will be displayed using the defaults specified in the dimension style. You can use the XML tags to override the default style and apply style overrides for all or portions of the text.
The formatting overrides are defined using tags. There is an opening tag and closing tag for each formatting override you define. The text between the opening and closing tags is affected by the override.

## Syntax

ModelHoleThreadNoteDefinition.**FormattedHoleThreadNote**() As String

## Property Value

This is a read/write property whose value is a String.

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |