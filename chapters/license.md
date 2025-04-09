#  Software Licenses

Generaly, licenses define how project materials (software, data, documents, etc.) can be used and redistributed.
If the license or a publication agreement makes it difficult for people to contribute, the project is less likely to attract new members, 
so the choice of license is crucial to the project's long-term sustainability.

> **Open Except...**
>
> Projects that are only developing software may not have any problem making everything open.
> Teams working with sensitive data, on the other hand,
> must be careful to ensure that what should be private isn't inadvertently shared.
> In particular,
> people who are new to Git (and even people who aren't)
> occasionally add raw data files containing personal identifying information to repositories.
> It's possible to rewrite the project's history to remove things when this happens,
> but that doesn't automatically erase copies people may have in forked repositories.

Every creative work has some sort of license;
the only question is whether authors and users know what it is and choose to enforce it.
Choosing a license for a project can be complex,
not least because the law hasn't kept up with everyday practice.
{cite:p}`Mori2012` and {cite:p}`Vand2014` are good starting points
to understand licensing and intellectual property from a researcher's point of view, while {cite:p}`Lind2008` is a deeper dive for those who want details.
Depending on country, institution, and job role, most creative works are automatically eligible for intellectual property protection.
However, members of the team may have different levels of copyright protection.
For example, students and faculty may have a copyright on the research work they produce, but university staff members may not, since their employment agreement may state that what they create on the job belongs to their employer.

To avoid legal messiness, every project should include an explicit license.
This license should be chosen early, since changing a license can be complicated. For example, each collaborator may hold copyright on their work
and therefore need to be asked for approval when a license is changed.
Similarly, changing a license does not change it retroactively,
so different users may wind up operating under different licensing structures.

> **Leave It to the Professionals**
>
> Don't write your own license.
> Legalese is a highly technical language,
> and words don't mean what you think they do.

To make license selection for code as easy as possible,
GitHub allows us to select one of several common software licenses when creating a repository.
The Open Source Initiative maintains [a list](https://opensource.org/licenses) of **open licenses**,
and [choosealicense.com](https://choosealicense.com/) will help us find a license that suits our needs. Some of the things we need to think about are:

1.  Do we want to license the work at all?
2.  Is the content we are licensing source code?
3.  Do we require people distributing derivative works to also distribute their code?
4.  Do we want to address patent rights?
5.  Is our license compatible with the licenses of the software we depend on?
6.  Do our institutions have any policies that may overrule our choices?
7.  Are there any copyright experts within our institution who can assist us?

Unfortunately,GitHub's list does not include common licenses for data or written works like papers and reports. 
Those can be added in manually, but it's often hard to understand the interactions among multiple licenses on different kinds of material {cite:p}`Alme2017`.

Just as the project's Code of Conduct is usually placed in a root-level file called `CONDUCT.md`, its license is usually put in a file called `LICENSE.md` that is also in the project's root directory.

## Licenses

Software licenses are crucial tools for both creators and users, they can be outlined as follows:

**Software as Intellectual Property**:

Like artwork, designs, and texts, software is considered intellectual property, a creation of the human mind deserving legal protection. This protection prevents unauthorized use and copying, giving creators control over their work.

**Common Forms of Protection**:

Copyright is the primary form of legal protection for software, safeguarding its code and functionality. Other relevant forms include patents (for unique algorithms or processes) and trade secrets (for confidential information).

**Software Licenses: Contracts for Use**:

A software license acts as a legal agreement between the owner (licensor) and the user (licensee). It grants permission to use the software under specific terms and conditions outlined in the agreement.

**What Licenses Define**:

Licenses typically specify: 

- The number of permitted installations.
- Commercial or non-commercial use allowed.
- Modification or distribution rights.
- Warranties and liabilities of the licensor.

**Importance of Licenses**:

Without a license, using copyrighted software is illegal. Licenses ensure legal and ethical use, protecting both creators and users.


There are numerous types of software licenses, ranging from free and open-source (e.g., GNU GPL) to paid commercial licenses with varying restrictions.
Understanding license terms is crucial before installing or using any software.
Breaching license terms can have legal consequences.

It is important think of Licenses when working with software, since they are vital for responsible and legal software use. Always take the time to read and understand the terms before using any software!

Fortunately, while there are a lot of different software licenses, there are only a few standard ones used.

### Types of software licenses

In general, there are three types of licenses.

#### Permissive licenses:
Allow users to use, modify, and distribute the work under certain conditions. They typically have few restrictions and allow for combination with other licenses.

#### Copyleft licenses:
Require that derivative works or modifications of the work be distributed under the same license terms. They aim to ensure that any improvements or modifications made to the work remain freely available to the community.

#### Proprietary licenses: 
Grant limited rights to use the work under specific conditions defined by the owner. These licenses usually restrict the redistribution, and modification of the work, or reverse engineering in case of software.

### Software and Data licenses 

Both are relevant in the context of research data and software Tend to use similar yet different licenses. The distinction arises from the inherent differences in their nature and the legal considerations associated with them, such as:

- Software is creative work, data is factual information

- Software is subject to copyright law, data may also be subject to privacy laws (sensitive data)

- Software licenses govern usage, modification and distribution of source code or executables.
 
- Data licenses address questions of access, usage, and sharing. 

- Continuously evolving practice in both fields.


### Common Open Source Software Licenses

#### MIT License:

- Permissive license allowing users to freely use, modify, and distribute the software.

- Requires including the original license and copyright notice in the distribution.

- Provides flexibility for commercial and proprietary use.

- Does not impose copyleft requirements on derivative works.

- Compatible with other licenses, including copyleft licenses.

The also popular **BSD** license is quite similar.

#### Apache License:

- Permissive license allowing users to use, modify, and distribute the software under certain conditions.

- Requires including the original copyright notice and license in distributions.
- Provides patent protection through a patent grant clause.

- Compatible with other licenses, including copyleft licenses.

- Promotes the combination of open-source and commercial software.

#### GNU General Public License (GPL):

- Copyleft license that ensures derivative works are also licensed under the GPL.
- Requires distributing the source code of the software when distributing the software itself.
- Encourages sharing and collaboration within the open-source community.

- Version 2 (GPLv2) is widely used and compatible with GPLv3 but less compatible with other licenses.

- Version 3 (GPLv3) includes additional provisions for patent protection.

### Creative Commons (CC) Licenses 

CC license are: 
A set of licenses used primarily for creative works, including artwork, literature, and media. They also are frequently used for data and other scientific outputs, but not recommended for software or hardware.
Various CC licenses exist, with different combinations of attribution, share-alike, and non-commercial clauses. They provides a framework for granting permissions and specifying usage restrictions. CC licenses offer flexibility in allowing creators to define the terms of use and distribution for their works.

CC Licenses offer varying levels of flexibility and restrictions, allowing creators to choose the terms that align with their desired balance between openness and control:

- Public Domain (**CC0**)
- Attribution (**CC BY**)
- Attribution-ShareAlike (**CC BY-SA**)
- Attribution-NoDerivs (**CC BY-ND**)
- Attribution-NonCommercial (**CC BY-NC**)
- Attribution-NonCommercial-ShareAlike (**CC BY-NC-SA**)
- Attribution-NonCommercial-NoDerivs (**CC BY-NC-ND**)

All CC licenses can be found [here](https://creativecommons.org/licenses/)

### Which License should you choose? 

Which license is the most suitable for your situation depends on a number of aspects:

- Do we want to license the work at all?
- Is the content we are licensing source code?
- Do we require people distributing derivative works to also distribute their code?
- Do we want to address patent rights?
- Is our license compatible with the licenses of the software we depend on?
- Do our institutions have any policies that may overrule our choices?
- Are there any copyright experts within our institution who can assist us?

You can get more help at: [Choosealicense.com](https://choosealicense.com/) 

**IMPORTANT:** **_Don’t write your own license. Legalese is a highly technical language, and words don’t mean what you think they do._**

