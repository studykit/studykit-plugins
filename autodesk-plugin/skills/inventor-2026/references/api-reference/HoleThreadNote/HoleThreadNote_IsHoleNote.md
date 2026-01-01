# HoleThreadNote.IsHoleNote Property

Parent Object: [HoleThreadNote](../HoleThreadNote/HoleThreadNote.md)

## Description

Property that indicates if this note is for a hole or thread feature. Returns True if it is for a hole note. This is true even in the case where the hole is tapped and has threads. Returns False in the case where the note is for a thread feature. There is some difference in behavior between the two and this property provides a convenient way to determine the expected behavior.

## Syntax

HoleThreadNote.**IsHoleNote**() As Boolean

## Property Value

This is a read only property whose value is a Boolean.

## Version

Introduced in version 2010
