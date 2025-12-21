# FileDialog.InsertMode Property

Parent Object: [FileDialog](../FileDialog/FileDialog.md)

## Description

Gets and sets whether the FileDialog is being used for inserting a file (as opposed to opening one). If set to True, the OnFileInsertDialog event is fired by the ShowOpen method; if set to False, the OnFileOpenDialog event is fired. This defaults to True when a FileDialog is created.

## Syntax

FileDialog.**InsertMode**() As Boolean

## Property Value

This is a read/write property whose value is a Boolean.

## Version

Introduced in version 2009
