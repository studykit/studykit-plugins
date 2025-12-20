# ContentCenterRSCResultEnum Enumerator

## Description

Enum indicating result of refresh standard components process.

## Methods

|  |  |  |
| --- | --- | --- |
| Name | Value | Description |
| kRSCFamilyHealthMissingCatParamMap | 80179 | Warning: Family is sick. Missing category parameters map in family. Part has been skipped. |
| kRSCFamilyHealthOutOfDateWithAuthorTableAndCategory | 80183 | Warning: Family is sick. Family is in a bad shape. Part has been skipped. |
| kRSCFamilyHealthOutOfDateWithCategory | 80181 | Warning: Family is sick. Family requires re-author and missing parameters map. Part has been skipped. |
| kRSCFamilyHealthOutOfDateWithTable | 80180 | Warning: Family is sick. Family requires re-author and family table updated incompletely. Part has been skipped. |
| kRSCFamilyHealthOutOfDateWithTableAndCategory | 80182 | Warning: Family is sick. Family table has been updated incompletely and family is missing category parameters map. Part has been skipped. |
| kRSCFamilyHealthRequiresReAuthor | 80177 | Warning: Family is sick. Family requires re-author. Part has been skipped. |
| kRSCFamilyHealthTableUpdateIncomplete | 80178 | Warning: Family is sick. Family table updated incompletely. Part has been skipped. |
| kRSCInstancingDifferentFamily | 80195 | Warning: Instancing failed. Part is coming from different family. Part has been skipped. |
| kRSCInstancingDifferentMember | 80196 | Warning: Instancing failed. Part is coming from different member. Part has been skipped. |
| kRSCInstancingFeatureSuppressFail | 80199 | Warning: Instancing failed. Suppress/unsuppress feature failed. Part has been skipped. |
| kRSCInstancingInvalidMemberValue | 80202 | Warning: Instancing failed. Invalid member value for column. Part has been skipped. |
| kRSCInstancingLongFilename | 80198 | Warning: Instancing failed. Part file name exceeds allowed length. Part has been skipped. |
| kRSCInstancingMaterialNotFound | 80197 | Warning: Instancing failed. Missing material. Part has been skipped. |
| kRSCInstancingMissingFileWritePermission | 80194 | Warning: Instancing failed. Missing file write permission. Part has been skipped. |
| kRSCInstancingThreadCreateFail | 80201 | Warning: Instancing failed. Failed to create thread/hole feature. Part has been skipped. |
| kRSCInstancingThreadFeatureNotFound | 80200 | Warning: Instancing failed. Missing thread/hole feature. Part has been skipped. |
| kRSCInstancingUnknownError | 80193 | Warning: Instancing failed. Unknown instancing error. Part has been skipped. |
| kRSCNoError | 80129 | Succeeded. |
| kRSCNoTPAddInLoadedForTPPart | 80162 | Info: Part is from Tube&Pipe while Tube&Pipe add-in is not loaded. Part has been skipped. |
| kRSCPartIsTPPipe | 80161 | Info: Pipes from Tube&Pipe are excluded from refreshing. Part has been skipped. |
| kRSCReplaceFailed | 80209 | Warning: New part has been created, but replacing of part failed. Part has been skipped. |
| kRSCUnknownFailed | 80145 | Error: Unknown fail. Check the assembly for consistency. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |