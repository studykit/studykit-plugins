# ModelHoleThreadNoteDefinition.UseParameterTolerance Property

Parent Object: [ModelHoleThreadNoteDefinition](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition.md)

## Description

Read-write property that gets and sets whether to use the format and tolerance information from parameters for hole note.
This is only valid for notes to hole features and not notes to thread features. This can easily be determined by checking the value of IsHoleNote property. In other cases the value of this property should be ignored and setting it will fail.

## Syntax

ModelHoleThreadNoteDefinition.**UseParameterTolerance**() As Boolean

## Property Value

This is a read/write property whose value is a Boolean.

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |