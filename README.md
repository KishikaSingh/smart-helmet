# Smart Helmet

A web application for the **Smart Helmet** project, deployed on an **AWS EC2 Ubuntu instance** using **Nginx** as the web server. This project demonstrates how to take a frontend application from development to a production-ready deployment on Linux.

---

## Project Overview

The Smart Helmet project is designed as a web interface for a smart helmet solution. The application was developed locally and deployed to an Ubuntu server hosted on AWS EC2 using Nginx.

This project focuses on:

- Frontend application deployment
- Linux server administration
- Nginx web server configuration
- Production hosting on AWS EC2
- Basic DevOps deployment workflow

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Frontend | HTML, CSS, JavaScript |
| Web Server | Nginx |
| Operating System | Ubuntu Linux |
| Cloud Platform | AWS EC2 |
| Remote Access | SSH |
| Version Control | Git & GitHub |

---

## Architecture

```
                 Developer Machine
                        │
                 Git Push to GitHub
                        │
                        ▼
               AWS EC2 Ubuntu Instance
                        │
                 Git Clone Repository
                        │
                        ▼
               Project Files on Server
                        │
                        ▼
                  Nginx Web Server
                        │
                        ▼
                  Browser Access
```

---


# Deployment Workflow

## Step 1 — Launch an EC2 Instance

- Launch Ubuntu EC2 instance
- Configure Security Group

Open the following ports:

| Port | Purpose |
|------|----------|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS (optional) |

---

## Step 2 — Connect to the Instance

```bash
ssh -i your-key.pem ubuntu@<EC2-Public-IP>
```

---

## Step 3 — Update Ubuntu

```bash
sudo apt update
sudo apt upgrade -y
```

---

## Step 4 — Install Git

```bash
sudo apt install git -y
```

Verify installation

```bash
git --version
```

---

## Step 5 — Install Nginx

```bash
sudo apt install nginx -y
```

Start Nginx

```bash
sudo systemctl start nginx
```

Enable Nginx on boot

```bash
sudo systemctl enable nginx
```

Check status

```bash
sudo systemctl status nginx
```

---

## Step 6 — Clone Repository

```bash
git clone https://github.com/KishikaSingh/smart-helmet.git
```

Navigate into the project

```bash
cd smart-helmet
```

---

## Step 7 — Deploy Website

Remove the default Nginx webpage

```bash
sudo rm -rf /var/www/html/*
```

Copy project files

```bash
sudo cp -r * /var/www/html/
```

Alternatively

```bash
sudo cp -r . /var/www/html/
```

---

## Step 8 — Verify Nginx Configuration

```bash
sudo nginx -t
```

Expected output

```
syntax is ok
test is successful
```

---

## Step 9 — Restart Nginx

```bash
sudo systemctl restart nginx
```

---

## Step 10 — Access the Website

Open your browser

```
http://<EC2-Public-IP>
```

The Smart Helmet application should now be live.

---

# Nginx Commands Used

### Install

```bash
sudo apt install nginx -y
```

### Start

```bash
sudo systemctl start nginx
```

### Stop

```bash
sudo systemctl stop nginx
```

### Restart

```bash
sudo systemctl restart nginx
```

### Reload Configuration

```bash
sudo systemctl reload nginx
```

### Enable at Boot

```bash
sudo systemctl enable nginx
```

### Check Status

```bash
sudo systemctl status nginx
```

### Test Configuration

```bash
sudo nginx -t
```

---

# Git Commands Used

Clone repository

```bash
git clone https://github.com/KishikaSingh/smart-helmet.git
```

Navigate

```bash
cd smart-helmet
```

Pull latest changes

```bash
git pull origin main
```

---

# Linux Commands Used

Update packages

```bash
sudo apt update
```

Upgrade packages

```bash
sudo apt upgrade -y
```

List files

```bash
ls
```

Show current directory

```bash
pwd
```

Change directory

```bash
cd smart-helmet
```

Copy files

```bash
sudo cp -r * /var/www/html/
```

Remove files

```bash
sudo rm -rf /var/www/html/*
```

---

# Deployment Workflow Summary

```
Develop Application
        │
        ▼
Push Source Code to GitHub
        │
        ▼
Launch AWS EC2 Ubuntu Instance
        │
        ▼
Connect using SSH
        │
        ▼
Install Git
        │
        ▼
Install Nginx
        │
        ▼
Clone Repository
        │
        ▼
Copy Project Files to
/var/www/html
        │
        ▼
Restart Nginx
        │
        ▼
Application Available via
EC2 Public IP
```

---

# Key Learnings

- Hosting a static website using Nginx
- Deploying applications on AWS EC2
- Managing Linux servers through SSH
- Using Git for server-side deployments
- Configuring and managing Nginx services
- Understanding the Linux filesystem and web root
- Deploying production-ready static web applications

---

# Future Improvements

- Configure HTTPS using Let's Encrypt SSL
- Register and configure a custom domain
- Automate deployments with GitHub Actions
- Containerize the application using Docker
- Deploy behind an AWS Application Load Balancer
- Add CloudFront CDN for improved performance
- Implement CI/CD pipeline for automated deployments

---

# Author

**Kishika Singh**
