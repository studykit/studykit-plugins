# FileManagementEnum Enumerator

## Description

Bits indicating options used for various file management operations.

## Methods

|  |  |  |
| --- | --- | --- |
| Name | Value | Description |
| kCopyFileMask | 224 | Option used by CopyFile. |
| kDeleteFileMask | 1 | Option used by DeleteFile. |
| kForceFile | 1 | Option to force the deletion if the file is reserved. |
| kMoveFileMask | 225 | Option used by MoveFile. |
| kNoForceFile | 0 | Force option not specified. |
| kOverwriteExistingFile | 32 | Option to overwrite the existing file at the destination. |
| kOverwriteReadOnlyFile | 128 | Option to overwrite the existing read-only file at the destination. |
| kOverwriteReservedFile | 64 | Option to overwrite the existing file at the destination even if reserved. |

## Version

Introduced in version 6
